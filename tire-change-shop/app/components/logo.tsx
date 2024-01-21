import Image from 'next/image'

interface LogoProps {
    width: number;
}

export default function Logo({ width }: LogoProps) {
    return (
        <div>
            <Image
                src="/images/logo_filled.png"
                alt="Logo"
                width={width}
                height={width}
                className={"h-full"}
            />
        </div>
    )
}