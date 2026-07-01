import datetime
import json
import argparse
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from config import App_Configs as config
from pathlib import Path
import sys

def resource(relative):
    base_dir = Path(__file__).parent
    if getattr(sys, "frozen", False):
        base_dir = Path(sys.executable).parent
    return base_dir / relative

class ConfigManager:
    
    def __init__(self, file: str):
        self.file = file

    def read(self) -> dict | None:
        try:
            with open(self.file, "r", encoding="utf-8") as cfg:
                return json.load(cfg)
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Config file is corrupted or invalid JSON.")
        return None

    def write(self, key: str, value, subkey = None) -> None:
        config = self.read()

        if config is None:
            return
        if subkey is None:
            config[key] = value
        else:
            config[key][subkey] = value
        try:
            with open(self.file, "w", encoding="utf-8") as cfg:
                json.dump(config, cfg, indent=4)
        except OSError:
            print("Failed to write config file.")

class Normalizer:
    

    def __init__(self, config_manager: ConfigManager):
        self.cfg = config_manager
    
    def start(self) -> None:
        self.cfg.write("start", str(datetime.datetime.now()))
        print("Session started.")

    def __appTitle(self):
        title_text = Text(
            f"\n{config.APP_NAME.upper()} v{config.APP_VERSION} by {config.APP_AUTHOR}      \n", 
            style="white on blue", 
            justify="center"
        )
        app_panel = Panel.fit(
            title_text,
            border_style="blue",
            padding=0,
            
        )
        print(app_panel)

    def __printBar(self, max: int, progress: int, key: str, min_color: str, max_color: str) -> None:
        console = Console()
        color = f"[{min_color}]"
        max = max
        prog = progress

        filled = min(prog, max)
        overflow = prog - max
        bar = "■" * filled + "□" * (max - filled)
        if overflow >= 0:
            extra = f" +{overflow}" 
            color = f"[{max_color}]"
        else: 
            extra = ""
        console.print(f"{key}: {color}{bar}[/] {extra}")    
    
    def chech_status(self) -> None:
        console = Console()
        config = self.cfg.read()
        if config is None:
            return
        
        self.__appTitle()

        startDate = datetime.datetime.fromisoformat(config["start"])
        passedDays = (datetime.datetime.now() - startDate).days
        sections = [k for k in config if k != "start"]

        console.print(Panel(
            f"[bold white]Date:[/bold white] [cyan]{startDate}[/cyan]\n[bold white]Days:[/bold white] [cyan]{passedDays}[/cyan]",
            title="Overal Info:",
            expand=False,
            border_style="green"
        ))

        for section in sections:
            print(f"\n{section.capitalize()}")
            for key, val in config[section].items():
                if key.lower() == "x":
                    self.__printBar(val, passedDays, key.upper(), "magenta", "green")
                else:
                    self.__printBar(val, passedDays, key.upper(), "cyan", "green")


class CLI:
    def __init__(self):
        # self.cfg_manager = ConfigManager("./configs.cfg")
        self.cfg_manager = ConfigManager(
            str(resource("configs.cfg"))
        )


        self.normalizer = Normalizer(self.cfg_manager)
        self.parser = self._build_parser()
    
    def _build_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="The Habit Tracker CLI Version.")
        parser.add_argument("-s", "--start", help="Starts a new session.", action="store_true")
        parser.add_argument("-c", "--check", help="Check current status.", action="store_true")
        return parser
    
    def run(self) -> None:
        args = self.parser.parse_args()

        if not any(vars(args).values()):
            self.parser.print_help()
            return
        
        if args.start:
            self.normalizer.start()
        elif args.check:
            self.normalizer.chech_status()

if __name__ == "__main__":
    CLI().run()
