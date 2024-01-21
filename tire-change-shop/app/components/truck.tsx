import Image from 'next/image';

export default function Truck() {
    return (
        <div>
            <Image
                src="/images/truck.png"
                alt="Truck"
                width={600}
                height={600}
                className={"fixed bottom-5 right-0 z-[-1] transform rotate-90 translate-x-1/4 translate-y-1/4 opacity-50 transition duration-500 ease-in-out scroll-snap-align-start"}
            />
        </div>
    )
}