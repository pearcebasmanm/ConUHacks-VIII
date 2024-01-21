"use client"
// import Image from "next/image";
import Link from "next/link";
import { useState } from 'react';
import Logo from "./components/logo";

export default function Home() {

  return (
    // text-[#F9DC5C]
    <main className="flex flex-col items-center justify-around rounded-md">
      <Logo />
    </main>
  );
}
