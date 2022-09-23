import json
import sys

from SeleniumAction import SeleniumAction
from SeleniumDTO import SeleniumDTO
from TargetDTO import TargetDTO

json_string = sys.argv[1]

json_dict = json.loads(json_string)

selenium_dto = SeleniumDTO(
    arguments=json_dict["selenium"]["arguments"],
    fullscreen=json_dict["selenium"]["fullscreen"]
)

target_dto_list = []

for target in json_dict["targets"]:
    target_dto_list.append(
        TargetDTO(
            screenshot_filename=target["screenshot_filename"],
            html_output_filename=target["html_output_filename"],
            url=target["url"],
            timeout=target["timeout"],
            wait_for_xpath_element=target["wait_for_xpath_element"] if "wait_for_xpath_element" in target else None,
        )
    )

if __name__ == '__main__':

    selenium_action = SeleniumAction(selenium_dto, target_dto_list)
    selenium_action.run()
