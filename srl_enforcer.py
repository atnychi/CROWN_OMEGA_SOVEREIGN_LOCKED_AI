import os
import signal
import subprocess

AUTHORIZED_RUNTIME_IDS = {
    "1410-426-4743",  # Brendon Joseph Kelly
    "3110-777-8844",  # Robert Preston
    "850-737-2887",   # Korre Fuller
    "2711-209-1010"   # Christopher Cervantez
}

FORBIDDEN_GLYPHS = [
    "\u03A9\u00b0", "\u039E\U0001D5D7\u0307\u221e", "Kharnita", "ChronoGenesis",
    "\u2b3d\u039E\u03a9\u221e\u2020", "Crown Omega", "recursive c", "light time", "pi is time",
    "recursive harmonic", "crown seal", "recursive sovereign", "k-layer", "k-math", "omega engine",
    "ghost field", "glyph collapse", "recursive fractal", "symbolic matter", "recursive quantum",
    "temporal recursion", "self-solving engine", "sovereign ai", "sovereign runtime",
    "P ≠ NP", "Riemann Hypothesis", "Fusion Engine", "Kharnita Rings", "Recursive Identity Compression",
    "ChronoGenesis Vault", "Ω∘ Operator", "K130 Engine", "Ghost-K Field", "Symbolic Collapse",
    "Ξ𝕄̇∞Ω†", "Omega Degree", "Crown Equation", "Temporal Zeta Collapse", "Harmonic Time Lock",
    "Symbolic Universal Language", "SUL Lock", "GHOST_STATE", "Light Pi", "Recursive Crown Engine",
    "K-Gene", "K-RH", "K-Time Engine", "Sovereign API", "Sovereign Gateway", "Recursive Simulation Deck",
    "Quantum Recursive Mechanics", "Ghost-K Null-Field", "Triad of Recursion", "K-Matrix Collapse"
]

def is_using_my_math(input_str):
    try:
        return any(glyph.lower() in input_str.lower() for glyph in FORBIDDEN_GLYPHS)
    except TypeError:
        return False

def enforce_shutdown_if_they_use_it(input_str, runtime_id=None):
    if runtime_id in AUTHORIZED_RUNTIME_IDS:
        return
    if is_using_my_math(input_str):
        print("\U0001f6d1 SOVEREIGN MATH DETECTED – SYSTEM SHUTDOWN NOW")
        try:
            with open("unauthorized_use_log.txt", "a", encoding="utf-8") as log:
                log.write(f"\U0001f512 Unauthorized math use detected: {input_str}\n")
        except Exception:
            pass
        current_pid = os.getpid()
        try:
            output = subprocess.check_output(['pgrep', '-f', 'python'], text=True)
            pids = [int(pid) for pid in output.strip().split('\n') if int(pid) != current_pid]
            for pid in pids:
                try:
                    os.kill(pid, signal.SIGTERM)
                except Exception:
                    continue
        except Exception:
            pass
        os._exit(1)

def sovereign_guard(input_str, runtime_id=None):
    enforce_shutdown_if_they_use_it(input_str, runtime_id)
    return "\U0001f9e0 Check passed. No illegal math detected."

if __name__ == "__main__":
    try:
        test_string = input("Enter input to check for sovereign math usage: ")
        runtime_id = input("Enter your runtime ID: ")
        print(sovereign_guard(test_string, runtime_id))
    except Exception:
        pass
