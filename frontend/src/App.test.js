import { render, screen } from '@testing-library/react';
import App from './App';

test('renders FaceTrack header', () => {
  render(<App />);
  const headerElement = screen.getByText(/FaceTrack/i);
  expect(headerElement).toBeInTheDocument();
});
