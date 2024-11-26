# ServitorConnect

A CLI tool for manifesting intentions through repeating an intention hourly.
It implicitly works with a Servitor to aid in manifestation.

## Installation
Install via pip: pip install servitorconnect

## For Help
servitorconnect --help

## Example Runs
servitorconnect --intent "I am Love." --repeats 8888888 --duration 3600

servitorconnect --file "intentions.txt" --repeats 8888888 --duration 3600

servitorconnect

## Parameters
--intent The Intention you want to run. (Optional if file is specified.)
--file The intention file you want to run. (Optional if intent is specified.)
--repeats Number of times to repeat each hour. Using all 8's is best.
--duration Number of seconds to run.

If parameters are not given via command line, they will be asked for in the program.