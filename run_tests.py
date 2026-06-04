import subprocess


def run_tests():
    command = [
        ".venv/bin/python",
        "-m",
        "pytest",
        "-m",
        "smoke"
    ]

    subprocess.run(command, check=True)


if __name__ == "__main__":
    run_tests()