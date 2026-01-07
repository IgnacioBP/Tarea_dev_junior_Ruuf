from typing import List, Tuple, Dict
import json


def calculate_panels(panel_width: int, panel_height: int, 
                    roof_width: int, roof_height: int) -> int:
    
    def check_fit( roof_width: int, roof_height: int, panel_width: int, panel_height: int):

        quantity = (roof_width // panel_width) * (roof_height // panel_height)
        h_quantity = roof_height // panel_height
        w_quantity = roof_width // panel_width

        grid= [[0 for _ in range(roof_width)] for _ in range(roof_height)]
        
        for y in range( h_quantity*panel_height):
            for x in range( w_quantity*panel_width):
                grid[y][x] = 1
        p_wid = panel_height
        p_hei = panel_width

        for y in range(roof_height):
            for x in range(roof_width):
                if grid[y][x] == 0:
                    if y + p_hei - 1 < roof_height and x + p_wid - 1 < roof_width:
                        can_place = True
                        for dy in range(p_hei):
                            for dx in range(p_wid):
                                if grid[y + dy][x + dx] == 1:
                                    can_place = False
                                    break
                            if not can_place:
                                break
                        if can_place:
                            for dy in range(p_hei):
                                for dx in range(p_wid):
                                    grid[y + dy][x + dx] = 1
                            quantity += 1
                
                else:
                    pass

        return quantity

    chequed = False
    #Orientacion del panel 1
    if panel_width > roof_width or panel_height > roof_height:   
        panel_quantities_1 = 0
    else:   
        panel_quantities_1 = check_fit( roof_width, roof_height,panel_width, panel_height)
        chequed = True

    print(f"panel_quantities_1: {panel_quantities_1}")


    #orientacion del panel 2
    if panel_height > roof_width or panel_width > roof_height:
        panel_quantities_2 = 0
    else:
        if not chequed:
            panel_quantities_2 = check_fit( roof_width, roof_height,panel_height, panel_width)
        else:
            panel_quantities_2 = panel_quantities_1

    print(f"panel_quantities_2: {panel_quantities_2}")

    return max(panel_quantities_1, panel_quantities_2)





def run_tests() -> None:
    with open('test_cases.json', 'r') as f:
        data = json.load(f)
        test_cases: List[Dict[str, int]] = [
            {
                "panel_w": test["panelW"],
                "panel_h": test["panelH"],
                "roof_w": test["roofW"],
                "roof_h": test["roofH"],
                "expected": test["expected"]
            }
            for test in data["testCases"]
        ]
    
    print("Corriendo tests:")
    print("-------------------")
    
    for i, test in enumerate(test_cases, 1):
        result = calculate_panels(
            test["panel_w"], test["panel_h"], 
            test["roof_w"], test["roof_h"]
        )
        passed = result == test["expected"]
        
        print(f"Test {i}:")
        print(f"  Panels: {test['panel_w']}x{test['panel_h']}, "
              f"Roof: {test['roof_w']}x{test['roof_h']}")
        print(f"  Expected: {test['expected']}, Got: {result}")
        print(f"  Status: {'✅ PASSED' if passed else '❌ FAILED'}\n")


def main() -> None:
    print("🐕 Wuuf wuuf wuuf 🐕")
    print("================================\n")
    
    run_tests()


if __name__ == "__main__":
    main()