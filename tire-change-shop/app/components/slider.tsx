import React from 'react';

interface SliderComponentProps {
  value: number;
  onChange: (value: number) => void;
}

const SliderComponent: React.FC<SliderComponentProps> = ({ value, onChange }) => {
  return (
    <input
      type="range"
      min="0"
      max="100"
      value={value}
      onChange={(e) => onChange(parseInt(e.target.value))}
      className="slider" // Add your CSS class for styling
    />
  );
};

export default SliderComponent;
