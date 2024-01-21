import React, { useRef, useEffect } from 'react';

interface CanvasComponentProps {
  sliderValue: number; // Value from the slider to control the display
}

const CanvasComponent: React.FC<CanvasComponentProps> = ({ sliderValue }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas?.getContext('2d');
    if (context) {
      // Clear canvas
      context.clearRect(0, 0, canvas.width, canvas.height);

      // Draw items based on sliderValue
      // Example: Show/hide items or change their properties
      if (sliderValue > 50) {
        // Draw something
      } else {
        // Draw something else or leave it blank
      }

      // Add more drawing logic based on sliderValue
    }
  }, [sliderValue]);

  return <canvas ref={canvasRef} width={800} height={600} />;
};

export default CanvasComponent;
