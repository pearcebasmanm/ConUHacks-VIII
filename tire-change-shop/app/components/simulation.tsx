
// <motion.button
// style={{
//   fontSize: '20px', // make the button text bigger
//   padding: '10px 20px', // increase button size by padding
//   margin: 'auto', // center the button
//   display: 'block', // necessary for margin: auto to work
// }}
// whileHover={{ scale: 1.1 }} // animate button on hover
// whileTap={{ scale: 0.9 }} // animate button on tap
// >
// Start Simulation
// </motion.button>
// <div className="simulation hidden">
// <SliderComponent value={sliderValue} onChange={setSliderValue} />
// </div>

import { motion } from 'framer-motion';

export default function Simulation() {
    return (
        <motion.div className={"simulation-wrapper flex justify-center items-center border-1 border-[#111] text-xl"} style={{ height: `calc(100vh - 180px)` }}>
            <motion.button
                className={"font-mono text-[#F9DC5C] bg-[#2E2E2E] font-lg py-4 px-8 m-4"}
                whileHover={{ scale: 1.1, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}
                whileTap={{ scale: 0.9, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}

                onClick={e => {
                    document.querySelector('.simulation').classList.remove('hidden');
                    document.querySelector('.simulation').classList.add('flex');
                    e.target.classList.add('hidden');
                }}
            >
                Start Simulation
            </motion.button>
            <motion.div 
                className="simulation hidden w-screen h-screen fixed left-0 bg-[#2E2E2E] text-[#F9DC5C] flex justify-center items-center"
                initial={{ opacity: 0, top: 100, scale: 0.9 }}
                animate={{ opacity: 1, top: 0, scale: 1 }}
                transition={{ duration: 1 }}
            >
                <motion.button
                    className={"font-mono text-[#F9DC5C] bg-[#2E2E2E] font-lg py-4 px-8 m-4 absolute top-0 right-0"}
                    whileHover={{ scale: 1.1, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}
                    whileTap={{ scale: 0.9, backgroundColor: '#F9DC5C', color: '#2E2E2E' }}

                    onClick={e => {
                        document.querySelector('.simulation').classList.remove('flex');
                        document.querySelector('.simulation').classList.add('hidden');
                        document.querySelector('.simulation-wrapper button').classList.remove('hidden');
                    }}
                >
                    Close
                </motion.button>
                <div className={"slider-container"}>
                    <input
                    type="range"
                    min="0"
                    max="100"
                    className="slider"
                    />
                </div>
            </motion.div>
        </motion.div>
    )    
}