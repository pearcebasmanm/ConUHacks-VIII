import Logo from './logo';

export default function AdminNav() {
    return (
        <nav className="flex justify-between items-center h-16 bg-[#2E2E2E] text-[#F9DC5C] relative shadow-sm font-mono mx-64" role="navigation">
            <a href="/" className="pl-8">
                <Logo width={100} />
            </a>
            <div className={`pr-8 menu`}>
                <a href="/" className="p-4">
                    The Bays
                </a>
                <a href="/about" className="p-4">
                    About Us
                </a>
            </div>
        </nav>
    );
}