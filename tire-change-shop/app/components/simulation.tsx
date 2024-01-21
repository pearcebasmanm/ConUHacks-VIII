"use client"
import { useState, useEffect } from 'react';
import { motion, useAnimation } from 'framer-motion';

interface Entry {
    name: string;
    start: number;
    duration: number;
}

export default function Simulation() {
    const speed = 0.02;
    let [time, setTime] = useState<number>(0);

    let [simulationStarted, setSimulationStarted] = useState<boolean>(false);
    let [isPlaying, setIsPlaying] = useState<boolean>(false);

    const [data, setData] = useState<Entry[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);


    if (isPlaying) {
        setTimeout(() => {
            if (time >= 1000) {
                setTime(0);
                setIsPlaying(false);
                return;
            }
            setTime(time + speed);
        }, speed);
    }

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await fetch('/api/data');
                if (!res.ok) { throw new Error(res.statusText) }

                const data : Entry[] = await res.json();
                setData(data);
            } catch (error : any) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        }

        fetchData();
    }, [])

    if (loading) {
        return (
            <div className={"flex justify-center items-center w-full h-screen"}>
                <motion.button
                    className={`font-mono text-[#F9DC5C] bg-[#2E2E2E] font-lg py-4 px-8 m-4 ${simulationStarted ? 'hidden' : 'block'}`}
                    whileHover={{ scale: 1.1, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}
                    whileTap={{ scale: 0.9, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}
                >
                    Loading...
                </motion.button>
            </div>
        )
    }

    if (error) {
        return (
            <div className={"flex justify-center items-center w-full h-screen"}>
                <div className={"font-mono text-[#F9DC5C] font-lg py-4 pr-8 flex items-center"}>
                    {error}
                </div>
            </div>
        )
    }

    return (
        <motion.div className={"simulation-wrapper flex justify-center items-center border-1 border-[#111] text-xl"} style={{ height: `calc(100vh - 180px)` }}>
            <motion.button
                className={`font-mono text-[#F9DC5C] bg-[#2E2E2E] font-lg py-4 px-8 m-4 ${simulationStarted ? 'hidden' : 'block'}`}
                whileHover={{ scale: 1.1, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}
                whileTap={{ scale: 0.9, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}

                onClick={ e => { setSimulationStarted(true) } }
            >
                Start Simulation
            </motion.button>
            <motion.div 
                className={`simulation ${simulationStarted ? 'block' : 'hidden'} w-screen h-screen fixed left-0 bg-[#2E2E2E] text-[#F9DC5C] flex justify-center items-center`}
                initial={{ opacity: 0, top: 100, scale: 0.9 }}
                animate={{ opacity: 1, top: 0, scale: 1 }}
                transition={{ duration: 1 }}
            >
            <motion.button
                className={"font-mono text-[#F9DC5C] bg-[#2E2E2E] font-lg py-4 px-8 m-4 absolute top-0 right-0"}
                whileHover={{ scale: 1.1, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}
                whileTap={{ scale: 0.9, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}
                onClick={e => window.location.reload()}
            >
                Exit
            </motion.button>

            <div className={"top-5 left-20 absolute date-picker"}>
                <div className={"font-mono text-[#F9DC5C] font-lg py-4 pr-8 flex items-center"}>
                    <div className={"mr-4"}>Date:</div>
                    <input
                        type="date"
                        className={"form-input cursor-pointer bg-transparent px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring focus:border-blue-300 transition duration-300 bg-opacity-0"}
                    />
                </div>
            </div>

            <div className={"slider-container fixed top-20 flex justify-center items-center font-mono"}>
                <div 
                    className={"font-mono text-[#F9DC5C] font-lg py-4 pr-8 flex items-center cursor-pointer"}
                    onClick={e => { setIsPlaying(!isPlaying) } }
                    >
                        Click
                </div>
                <div className={"w-full relative"}>
                    <div className={"absolute time-indicator first"}>|<br></br>7 AM</div>
                    <div className={"absolute time-indicator half"}>|<br></br>12 PM</div>
                    <div className={"absolute time-indicator last"}>|<br></br>7 PM</div>
                    <input
                        type="range"
                        min="0"
                        max="1000"
                        className="slider w-full"
                        value={time}
                        readOnly
                    />
                </div>
            </div>

            {data.map((schedule, index) => {
                return (
                    <motion.div
                        key={index}
                        className={"schedule"}
                        animate={{ left: `${schedule.start}%`, width: `${schedule.duration}%` }}
                        transition={{ duration: 1 }}
                    >
                        <div className={"schedule-text"}>{schedule.name}</div>
                    </motion.div>
                )
            } )}

            <div className={"bays-container flex justify-center items-center font-mono"}>
                <motion.div className={"bay bay-1 flex justify-center items-center"}>
                    <div className={"bay-number"}>1</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-2 flex justify-center items-center"}>
                    <div className={"bay-number"}>2</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-3 flex justify-center items-center"}>
                    <div className={"bay-number"}>3</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-4 flex justify-center items-center"}>
                    <div className={"bay-number"}>4</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-5 flex justify-center items-center"}>
                    <div className={"bay-number"}>5</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-6 flex justify-center items-center"}>
                    <div className={"bay-number"}>6</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-7 flex justify-center items-center"}>
                    <div className={"bay-number"}>7</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-8 flex justify-center items-center"}>
                    <div className={"bay-number"}>8</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-9 flex justify-center items-center"}>
                    <div className={"bay-number"}>9</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
                <motion.div className={"bay bay-10 flex justify-center items-center"}>
                    <div className={"bay-number"}>10</div>
                    <div className={"bay-vehicle"}></div>
                </motion.div>
            </div>
        </motion.div>
    </motion.div>
    )    
}