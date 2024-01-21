"use client"
import { useState } from 'react';
import AdminNav from "./components/admin-nav";
import Simulation from "./components/simulation";

export default function Home() {
  const [sliderValue, setSliderValue] = useState<number>(50);

  return (
    // text-[#F9DC5C] bg-[#2E2E2E]
    <main>
      <AdminNav />
      <Simulation />
    </main>
  );
}
