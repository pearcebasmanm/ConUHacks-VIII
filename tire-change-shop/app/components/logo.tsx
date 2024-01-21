import Image from 'next/image'

export default function Logo() {
  return (
    <div>
      <Image
        src="/images/logo_filled.png"
        alt="Logo"
        width={150}
        height={150}
      />
    </div>
  )
}