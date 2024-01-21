"use client"
// import Image from "next/image";
import Link from "next/link";
import { useState } from 'react';

export default function Home() {

  return (
    // text-[#F9DC5C]
    <main className="flex min-h-screen flex-col items-center justify-around p-24 rounded-md bg-[#465362]">
      {/* <div className="w-full flex justify-around">
        <h2 className="text-2xl">
          Tire Change Shop
        </h2>
        <div className="flex gap-x-6 items-center">
          <h3 className="text-xl">
            <Link href="/">Home</Link>
          </h3>
          <h3 className="text-xl">
            <Link href="/about">About</Link>
          </h3>
          <h3 className="text-xl">
            <Link href="/contact_us">Contact Us</Link>
          </h3>
        </div>
      </div>
      <div className="w-full flex justify-around">
        active: shadow-[0_2px_#f5d453] active: translate-y-[3px] *
        <button className="bg-[#ffd639] hover:bg-[#ffdf5e] shadow-[0_5px_#ffdf60] hover:shadow-[#f3da78] active:shadow-[0_2px_#ffdf60] active:translate-y-[3px] text-black p-2 rounded-xl">Gold</button>
        <button className="bg-[#ffd639] hover:bg-[#ffdf5e] shadow-[0_5px_#ffdf60] hover:shadow-[#f3da78] active:shadow-[0_2px_#ffdf60] active:translate-y-[3px] text-black p-2 rounded-xl">Gold</button>
        <button className="bg-[#ffd639] hover:bg-[#ffdf5e] shadow-[0_5px_#ffdf60] hover:shadow-[#f3da78] active:shadow-[0_2px_#ffdf60] active:translate-y-[3px] text-black p-2 rounded-xl">Gold</button>
      </div> */}
      {/* <table>
        <thead>

        </thead>
      </table> */}
      <div>
        <h1>Pick a date</h1>
        <label htmlFor="dateofbirth"></label>
        <input type="date" name="date" id="dateofbirth"></input>
      </div>
      <select>
        <option value="CompactCars">Compact Cars</option>
        <option value="MediumCars">Medium Cars</option>
        <option value="FullSizeCars">Full Size Cars</option>
        <option value="Class1_Trucks">Class 1 Trucks</option>
        <option value="Class2_Trucks">Class 2 Trucks</option>
      </select>
    </main>
  );
}
