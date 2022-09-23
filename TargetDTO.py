from dataclasses import dataclass


@dataclass
class TargetDTO:
    screenshot_filename: str
    html_output_filename: str
    url: str
    timeout: int
    wait_for_xpath_element: str = None
