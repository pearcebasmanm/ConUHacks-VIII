export default function AdminNav() {
    return (
        <nav className="flex justify-between items-center h-16 bg-[#2E2E2E] text-[#F9DC5C] relative shadow-sm font-mono" role="navigation">
            <a href="#" className="pl-8">
                Admin
            </a>
            <div className={`pr-8 menu`}>
                <a href="#" className="p-4">
                    Dashboard
                </a>
                <a href="#" className="p-4">
                    The Bays
                </a>
            </div>
        </nav>
    );
}