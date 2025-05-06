from typing import List, Tuple, Dict
from typing import List, Tuple, Dict

def validate_name(name: str) -> str:
    """Return the first character of the name in uppercase."""
    return name[0].upper()

def char_to_ascii(char: str) -> int:
    """Convert a character to its ASCII value."""
    return ord(char)

def decimal_to_binary(decimal: int, bits: int) -> str:
    """Convert decimal to binary with specified bit length."""
    binary = bin(decimal)[2:]
    return binary.zfill(bits)[-bits:] if len(binary) > bits else binary.zfill(bits)

def xor_bits(bits: List[int]) -> int:
    """Perform XOR operation on a list of bits: 0^0=0, 1^1=0, 0^1=1, 1^0=1."""
    result = bits[0]
    for bit in bits[1:]:
        result ^= bit  # Standard XOR: 0^0=0, 1^1=0, 0^1=1, 1^0=1
    return result

def lfsr_simulation(initial_state: str, steps: int) -> Tuple[List[str], List[Dict]]:
    """Simulate LFSR process using XOR of first (bit 0) and last (bit 7) bits."""
    state = list(initial_state)
    output_sequence = []
    history = []

    # Initial state (Iteration 0)
    history.append({
        'Iteration': 0,
        'State': ''.join(state),
        'Output': '-',
        'Feedback': '-',
        'New State': ''.join(state)
    })

    for step in range(1, steps + 1):
        output_bit = state[-1]
        output_sequence.append(output_bit)

        # Calculate feedback using XOR of bit 0 (first) and bit 7 (last)
        selected_bits = [int(state[0]), int(state[-1])]  # Bit ke-0 dan ke-7
        feedback = xor_bits(selected_bits)

        # Shift state and insert feedback
        new_state = [str(feedback)] + state[:-1]

        history.append({
            'Iteration': step,
            'State': ''.join(state),
            'Output': output_bit,
            'Feedback': str(feedback),
            'New State': ''.join(new_state)
        })

        state = new_state

    return output_sequence, history