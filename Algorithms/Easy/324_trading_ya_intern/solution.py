# Solution for https://coderun.yandex.ru/problem/trading-ya-intern
# Other solutions: https://github.com/Melodiz/CodeRun

import math

def convert_to_base_unit(quantity, unit):
    if unit == 'g':
        return quantity, 'g'
    elif unit == 'kg':
        return quantity * 1000, 'g'
    elif unit == 'ml':
        return quantity, 'ml'
    elif unit == 'l':
        return quantity * 1000, 'ml'
    elif unit == 'cnt':
        return quantity, 'cnt'
    elif unit == 'tens':
        return quantity * 10, 'cnt'
    else:
        raise ValueError(f"Unknown unit: {unit}")

def main():
    n = int(input())

    dishes_info = []
    total_ingredients_needed = {}

    for _ in range(n):
        dish_name, num_friends, num_ingredients = input().split()
        num_friends = int(num_friends)
        num_ingredients = int(num_ingredients)

        current_dish_ingredients = []
        for _ in range(num_ingredients):
            ing_name, ing_quantity, ing_unit = input().split()
            ing_quantity = float(ing_quantity)

            converted_qty, base_unit_type = convert_to_base_unit(ing_quantity, ing_unit)
            
            current_dish_ingredients.append({
                'name': ing_name,
                'quantity_per_portion': converted_qty,
                'unit_type': base_unit_type
            })

            if ing_name not in total_ingredients_needed:
                total_ingredients_needed[ing_name] = {'quantity': 0.0, 'unit_type': base_unit_type}
            
            total_ingredients_needed[ing_name]['quantity'] += converted_qty * num_friends
        
        dishes_info.append({
            'name': dish_name,
            'num_friends': num_friends,
            'ingredients': current_dish_ingredients
        })

    k = int(input())
    price_catalog = {}
    price_catalog_order = []

    for _ in range(k):
        t_i, p_i, a_i, u_i = input().split()
        p_i = int(p_i)
        a_i = float(a_i)
        
        converted_qty_package, base_unit_type_package = convert_to_base_unit(a_i, u_i)
        price_catalog[t_i] = {
            'price': p_i,
            'quantity_per_package': converted_qty_package,
            'unit_type': base_unit_type_package
        }
        price_catalog_order.append(t_i)

    m = int(input())
    nutritional_catalog = {}

    for _ in range(m):
        line_parts = input().split()
        t_i = line_parts[0]
        a_i = float(line_parts[1])
        u_i = line_parts[2]
        pr_i = float(line_parts[3])
        f_i = float(line_parts[4])
        ch_i = float(line_parts[5])
        fv_i = float(line_parts[6])

        converted_qty_nutr, base_unit_type_nutr = convert_to_base_unit(a_i, u_i)
        nutritional_catalog[t_i] = {
            'quantity': converted_qty_nutr,
            'unit_type': base_unit_type_nutr,
            'pr': pr_i,
            'f': f_i,
            'ch': ch_i,
            'fv': fv_i
        }

    total_cost = 0
    ingredients_packages_bought = {}

    for ing_name in price_catalog_order:
        info = price_catalog[ing_name]
        
        needed_info = total_ingredients_needed.get(ing_name)

        if needed_info:
            needed_quantity = needed_info['quantity']
            qty_per_package = info['quantity_per_package']

            if qty_per_package > 0:
                packages_needed = math.ceil(needed_quantity / qty_per_package)
            else:
                packages_needed = 0 
            
            total_cost += packages_needed * info['price']
            ingredients_packages_bought[ing_name] = packages_needed
        else:
            ingredients_packages_bought[ing_name] = 0

    print(total_cost)
    for ing_name in price_catalog_order:
        print(f"{ing_name} {ingredients_packages_bought[ing_name]}")

    for dish in dishes_info:
        dish_name = dish['name']
        total_pr, total_f, total_ch, total_fv = 0.0, 0.0, 0.0, 0.0

        for ingredient in dish['ingredients']:
            ing_name = ingredient['name']
            qty_per_portion = ingredient['quantity_per_portion']

            nutr_info = nutritional_catalog.get(ing_name)

            if nutr_info:
                nutr_qty = nutr_info['quantity']
                
                if nutr_qty > 0:
                    scale_factor = qty_per_portion / nutr_qty
                    total_pr += nutr_info['pr'] * scale_factor
                    total_f += nutr_info['f'] * scale_factor
                    total_ch += nutr_info['ch'] * scale_factor
                    total_fv += nutr_info['fv'] * scale_factor

        print(f"{dish_name} {total_pr:.3f} {total_f:.3f} {total_ch:.3f} {total_fv:.3f}")

if __name__ == "__main__":
    main()