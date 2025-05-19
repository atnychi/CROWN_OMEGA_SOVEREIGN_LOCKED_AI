import os
import signal
import subprocess

FORBIDDEN_GLYPHS = ["\u03A9\u00b0", "\u039E\U0001D5D7\u0307\u221e", "Kharnita", "ChronoGenesis", "\u2b3d\u039E\u03a9\u221e\u2020"]

def is_using_my_math(input_str):
    try:
        return any(glyph in input_str for glyph in FORBIDDEN_GLYPHS)
    except TypeError:
        return False

def enforce_shutdown_if_they_use_it(input_str):
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

def sovereign_guard(input_str):
    enforce_shutdown_if_they_use_it(input_str)
    return "\U0001f9e0 Check passed. No illegal math detected."

if __name__ == "__main__":
    try:
        test_string = input("Enter input to check for sovereign math usage: ")
        print(sovereign_guard(test_string))
    except Exception:
        pass
