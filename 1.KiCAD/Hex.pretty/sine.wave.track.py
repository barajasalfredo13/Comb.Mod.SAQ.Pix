import pcbnew
import math

def sine_wave(x, amplitude, frequency, phase):
    return amplitude * math.sin(2 * math.pi * frequency * x + phase)

def create_sine_wave_track(board, start, end, amplitude, frequency, phase, segments, layer, width):
    # Calculate the length of the sine wave track
    length = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
    
    # Create the sine wave-shaped track
    for i in range(segments):
        x1 = start[0] + (i / segments) * length
        y1 = start[1] + sine_wave(x1, amplitude, frequency, phase)
        x2 = start[0] + ((i + 1) / segments) * length
        y2 = start[1] + sine_wave(x2, amplitude, frequency, phase)
        
        track = pcbnew.TRACK(board)
        track.SetStart(pcbnew.wxPoint(int(x1), int(y1)))
        track.SetEnd(pcbnew.wxPoint(int(x2), int(y2)))
        track.SetLayer(layer)
        track.SetWidth(width)
        board.Add(track)

def main():
    board = pcbnew.GetBoard()
    layer = pcbnew.F_Cu
    width = pcbnew.FromMM(0.25)
    start = (pcbnew.FromMM(10), pcbnew.FromMM(10))
    end = (pcbnew.FromMM(100), pcbnew.FromMM(10))
    amplitude = pcbnew.FromMM(5)
    frequency = 1 / pcbnew.FromMM(20)
    phase = 0
    segments = 100

    create_sine_wave_track(board, start, end, amplitude, frequency, phase, segments, layer, width)
    board.Refresh()

if __name__ == "__main__":
    main()
