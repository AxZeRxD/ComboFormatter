import os
from datetime import datetime
from pystyle import Colors, Colorate, Center
from Leveragers import log

class ComboFormatter:
    def __init__(self):
        self.datestr = datetime.now().strftime("%Y-%m-%d-%H-%M")
        self.outputdir = f"{self.datestr}"
        self.setupdirs()

    def setupdirs(self):
        os.makedirs(self.outputdir, exist_ok=True)

    def detectformat(self, sample):
        formats = {
            'GPT': {'pattern': lambda p: p[0].count('@') > 0 and p[1].count('@') == 0},
            'PGT': {'pattern': lambda p: p[1].count('@') > 0 and p[0].count('@') == 0},
            'TGP': {'pattern': lambda p: p[1].count('@') > 0 and p[2].count('@') == 0},
            'GTP': {'pattern': lambda p: p[0].count('@') > 0 and p[2].count('@') == 0},
            'TPG': {'pattern': lambda p: p[2].count('@') > 0 and p[1].count('@') == 0},
            'PTG': {'pattern': lambda p: p[1].count('@') > 0 and p[2].count('@') > 0}
        }

        parts = sample.split(':')
        if len(parts) != 3:
            return None

        for fmt, check in formats.items():
            try:
                if check['pattern'](parts):
                    return fmt
            except:
                continue
        return None

    def parsecombo(self, line, inputformat):
        parts = line.split(':')
        if len(parts) != 3:
            return None

        formatmap = {
            'GPT': {'gmail': 0, 'pass': 1, 'token': 2},
            'PGT': {'pass': 0, 'gmail': 1, 'token': 2},
            'TGP': {'token': 0, 'gmail': 1, 'pass': 2},
            'GTP': {'gmail': 0, 'token': 1, 'pass': 2},
            'TPG': {'token': 0, 'pass': 1, 'gmail': 2},
            'PTG': {'pass': 0, 'token': 1, 'gmail': 2}
        }

        if inputformat not in formatmap:
            return None

        mapping = formatmap[inputformat]
        return {
            'gmail': parts[mapping['gmail']],
            'pass': parts[mapping['pass']],
            'token': parts[mapping['token']]
        }

    def displaymenu(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        banner = """

                            
                         ██████╗ ██████╗ ███╗   ███╗██████╗  ██████╗ 
                        ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██╔═══██╗
                        ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║
                        ██║     ██║   ██║██║╚██╔╝██║██╔══██╗██║   ██║
                        ╚██████╗╚██████╔╝██║ ╚═╝ ██║██████╔╝╚██████╔╝
                        ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝  ╚═════╝ 
                                                                    
        ╔══════════════════════════════════════════════════════════════════════════╗
        ║    TOOL - COMBO FORMATTER  | BY - LEVERAGERS   |  PRESS "I" FOR INFO     ║
        ╚══════════════════════════════════════════════════════════════════════════╝

                    [01] P:G:T   [02] G:P:T    [03] T:G:P    [04] G:T:P 
                    [05] T:P:G   [06] P:T:G    [07] TOKEN    [08] G:P
                    [09] P:T     [10] T:P      [11] G:T      [12] P:G

        ╔══════════════════════════════════════════════════════════════════════════╗
        ║  DISCORD.GG/PROGRAMMERS    GITHUB - AxZeRxD    DISCORD - @Aizer.fr#0000  ║
        ╚══════════════════════════════════════════════════════════════════════════╝

        """

        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(banner)))
        user_input = log.inp("Option: ").strip()

        if user_input.lower() == 'i':
            self.displayinfo()
            return self.displaymenu()
        elif user_input == '':
            return self.displaymenu()
        else:
            return int(user_input)

    def displayinfo(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        info = """
        ╔══════════════════════════════════════════════════════════════════════════╗
        ║                           TOOL INFORMATION                               ║
        ║                                                                          ║
        ║  This tool formats combo lists into various formats based on user input. ║
        ║  Features:                                                               ║
        ║    - Detects combo format automatically.                                 ║
        ║    - Allows reformatting into 12 different formats.                      ║
        ║    - Outputs results into a timestamped directory.                       ║
        ║                                                                          ║
        ║  Usage:                                                                  ║
        ║    - Place your combos in a file named 'input.txt'.                      ║
        ║    - Run the tool and follow the menu instructions.                      ║
        ║                                                                          ║
        ║  Note:                                                                   ║
        ║    - The tool will automatically detect the input format.                ║
        ║    - The output will be saved in a directory named after the timestamp.  ║
        ║    - The tool will not overwrite existing files.                         ║
        ║    - P = PASSWORD, G = GMAIL, T = TOKEN                                  ║
        ║                                                                          ║    
        ║          BY LEVERAGERS    .GG/PROGRAMMERS     TEAM LEVERAEGRS            ║
        ╚══════════════════════════════════════════════════════════════════════════╝
        """
        print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(info)))
        input("Press Enter to return to the menu...")

    def formatcombos(self, combos, formattype, inputformat):
        formats = {
            1: lambda x: f"{x['pass']}:{x['gmail']}:{x['token']}",
            2: lambda x: f"{x['gmail']}:{x['pass']}:{x['token']}",
            3: lambda x: f"{x['token']}:{x['gmail']}:{x['pass']}",
            4: lambda x: f"{x['gmail']}:{x['token']}:{x['pass']}",
            5: lambda x: f"{x['token']}:{x['pass']}:{x['gmail']}",
            6: lambda x: f"{x['pass']}:{x['token']}:{x['gmail']}",
            7: lambda x: f"{x['token']}",
            8: lambda x: f"{x['gmail']}:{x['pass']}",
            9: lambda x: f"{x['pass']}:{x['token']}",
            10: lambda x: f"{x['token']}:{x['pass']}",
            11: lambda x: f"{x['gmail']}:{x['token']}",
            12: lambda x: f"{x['pass']}:{x['gmail']}"
        }

        if formattype not in formats:
            log.err("Invalid format type")
            return

        outputfile = f"{self.outputdir}/format{formattype}.txt"
        formatted = []

        for combo in combos:
            parsed = self.parsecombo(combo.strip(), inputformat)
            if parsed:
                try:
                    formatted.append(formats[formattype](parsed))
                except KeyError:
                    log.err(f"Failed to format: {combo}")
                    continue

        with open(outputfile, 'w') as f:
            f.write('\n'.join(formatted))

        log.success(f"Formatted {len(formatted)} combinations")

def main():
    formatter = ComboFormatter()

    try:
        with open("input.txt", 'r') as f:
            combos = f.readlines()
            if not combos:
                log.crit("Input file is empty")
                return

            inputformat = formatter.detectformat(combos[0].strip())
            if not inputformat:
                log.crit("Unable to detect input format")
                return

            log.success(f"Detected input format: {inputformat}")
            formattype = formatter.displaymenu()
            formatter.formatcombos(combos, formattype, inputformat)

    except FileNotFoundError:
        log.crit("input.txt not found")
    except Exception as e:
        log.crit(f"Error: {str(e)}")

if __name__ == "__main__":
    main()