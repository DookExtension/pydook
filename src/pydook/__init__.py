from argparse import ArgumentParser

__VERSION__ = '1.0.0'


def dook_exec(script: str, data: str) -> str:
    """Execute the script with data assigned to data.

    Execute the Python script provided in the script,
    assign the out variable within the script to data.

    Args:
        script (str): Python script to be executed
        data (str): Any type of file.

    Returns:
        str: The out variable, either data itself or possibly
        the script.
    """
    # By default out is data itself.
    out = data
    # Execute the script
    try:
        exec(script, {
            "data": data
        })
    except:
        out = data
    return out


def main():
    print('Hi.')
    parser = ArgumentParser(
        'Dook can be used to manipulate a data file and return the output')
    parser.add_argument('script', help='Path to script file.')
    parser.add_argument('data', help='Path to data file.')
    args = parser.parse_args()
    with open(args.script) as script_file:
        script = script_file.read()
    with open(args.data) as data_file:
        data = script_file.read()
    print(dook_exec(script, data))
