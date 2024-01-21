import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Truck from "./components/truck";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Tire Change Shop",
  description: "A brand that specializes in tire-changing services and values efficiency and speed.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>
        {children}
        <Truck />
      </body>

    </html>
  );
}
