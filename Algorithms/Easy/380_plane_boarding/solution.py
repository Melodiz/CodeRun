# Solution for https://coderun.yandex.ru/problem/plane-boarding
# Other solutions: https://github.com/Melodiz/CodeRun

def main():
    n = int(input())
    passengers_orig = []
    for i in range(n):
        line = input().split()
        a_i = int(line[0])
        row_seat_str = line[1]
        row_val = int(row_seat_str[:-1])
        seat_char = row_seat_str[-1]
        passengers_orig.append({
            "id": i,
            "a_i": a_i,
            "trg_r": row_val,
            "trg_s_char": seat_char,
            "trg_s_idx": "ABCDEF".index(seat_char),
            
            "cur_r": 0, 
            "state": "IN_QUEUE", 
            "action_finish_T": -1,
        })

    num_done = 0
    time = 0
    
    aisle_block_finish_T = [-1] * 31 
    seat_occupant = [[-1]*6 for _ in range(31)] 
    pass_in_aisle_at_row = [-1] * 31

    boarding_q_idx = 0
    max_time_passenger_seated = 0

    while num_done < n:
        # Phase 1: Complete actions scheduled for current `time`
        made_progress_in_phase1_outer_loop = True
        while made_progress_in_phase1_outer_loop:
            made_progress_in_phase1_outer_loop = False
            for p_idx in range(n):
                p = passengers_orig[p_idx]
                
                if p["state"] == "SEATED" or p["action_finish_T"] != time:
                    continue
                
                state_before_this_step = p["state"]
                action_T_before_this_step = p["action_finish_T"] # For debugging or more complex progress check
                
                current_passenger_processing_row = p["cur_r"] 

                if p["state"] == "MOVING":
                    if p["cur_r"] == p["trg_r"]: 
                        p["state"] = "STORING_LUGGAGE"
                        p["action_finish_T"] = time + p["a_i"] 
                        aisle_block_finish_T[p["cur_r"]] = max(aisle_block_finish_T[p["cur_r"]], p["action_finish_T"])
                        if pass_in_aisle_at_row[p["cur_r"]] != p_idx : 
                             pass_in_aisle_at_row[p["cur_r"]] = p_idx
                    else: 
                        p["state"] = "IDLE_IN_AISLE"
                        # action_finish_T remains `time`, but state change means they are now idle
                
                elif p["state"] == "STORING_LUGGAGE":
                    delay = 0
                    trg_r, trg_s_idx = p["trg_r"], p["trg_s_idx"]
                    
                    if p["trg_s_char"] == 'B': 
                        if seat_occupant[trg_r][2] != -1: delay = 5
                    elif p["trg_s_char"] == 'E': 
                        if seat_occupant[trg_r][3] != -1: delay = 5
                    elif p["trg_s_char"] == 'A': 
                        b_occ = seat_occupant[trg_r][1] != -1
                        c_occ = seat_occupant[trg_r][2] != -1
                        if b_occ and c_occ: delay = 15
                        elif b_occ or c_occ: delay = 5
                    elif p["trg_s_char"] == 'F': 
                        e_occ = seat_occupant[trg_r][4] != -1
                        d_occ = seat_occupant[trg_r][3] != -1
                        if e_occ and d_occ: delay = 15
                        elif e_occ or d_occ: delay = 5

                    if delay == 0:
                        p["state"] = "SEATED"
                        seat_occupant[trg_r][trg_s_idx] = p_idx
                        num_done += 1
                        max_time_passenger_seated = max(max_time_passenger_seated, time)
                        if pass_in_aisle_at_row[current_passenger_processing_row] == p_idx:
                             pass_in_aisle_at_row[current_passenger_processing_row] = -1
                    else:
                        p["state"] = "TAKING_SEAT"
                        p["action_finish_T"] = time + delay 
                        aisle_block_finish_T[trg_r] = max(aisle_block_finish_T[trg_r], p["action_finish_T"])
                
                elif p["state"] == "TAKING_SEAT":
                    p["state"] = "SEATED"
                    seat_occupant[p["trg_r"]][p["trg_s_idx"]] = p_idx
                    num_done += 1
                    max_time_passenger_seated = max(max_time_passenger_seated, time)
                    if pass_in_aisle_at_row[p["cur_r"]] == p_idx:
                        pass_in_aisle_at_row[p["cur_r"]] = -1
                
                if p["state"] != state_before_this_step or \
                   (p["state"] == state_before_this_step and p["action_finish_T"] != action_T_before_this_step and p["action_finish_T"] == time) : # Second condition for a_i=0 like cases
                    made_progress_in_phase1_outer_loop = True 
        
        if num_done == n:
            break

        passengers_making_decision_ids = []
        processed_for_decision_phase_ids = [False] * n

        for r_iter in range(30, 0, -1):
            p_id_in_aisle = pass_in_aisle_at_row[r_iter]
            if p_id_in_aisle != -1 and not processed_for_decision_phase_ids[p_id_in_aisle]:
                passenger_obj = passengers_orig[p_id_in_aisle]
                if passenger_obj["state"] == "IDLE_IN_AISLE":
                    passengers_making_decision_ids.append(p_id_in_aisle)
                    processed_for_decision_phase_ids[p_id_in_aisle] = True
        
        if boarding_q_idx < n:
            if not processed_for_decision_phase_ids[boarding_q_idx]: 
                 p_queue_head = passengers_orig[boarding_q_idx]
                 if p_queue_head["state"] == "IN_QUEUE": 
                    passengers_making_decision_ids.append(boarding_q_idx)
        
        aisle_targetted_for_t_plus_1 = [False] * 31
        planned_actions_for_t_plus_1 = [] 

        for p_idx in passengers_making_decision_ids:
            p = passengers_orig[p_idx]

            if not(p["state"] == "IDLE_IN_AISLE" or p["state"] == "IN_QUEUE"): # Only these states make new plans
                continue

            current_r = p["cur_r"]
            
            if p["state"] == "IDLE_IN_AISLE" and current_r == p["trg_r"] : 
                new_state_plan = "STORING_LUGGAGE"
                new_action_finish_T_plan = time + p["a_i"]
                aisle_to_block_plan = current_r
                block_until_T_plan = new_action_finish_T_plan
                
                planned_actions_for_t_plus_1.append((p_idx, new_state_plan, current_r, new_action_finish_T_plan, aisle_to_block_plan, block_until_T_plan))
                aisle_targetted_for_t_plus_1[aisle_to_block_plan] = True 
                continue 

            next_r_to_try = 0
            if current_r == 0: 
                next_r_to_try = 1
            elif p["state"] == "IDLE_IN_AISLE" and current_r < p["trg_r"]: 
                next_r_to_try = current_r + 1
            else: 
                continue 
            
            if next_r_to_try == 0 : continue

            if (aisle_block_finish_T[next_r_to_try] < time + 1) and \
               (not aisle_targetted_for_t_plus_1[next_r_to_try]): 
                
                new_state_plan = "MOVING"
                new_cur_r_plan = next_r_to_try
                new_action_finish_T_plan = time + 1 
                aisle_to_block_plan = new_cur_r_plan
                block_until_T_plan = time + 1 
                
                if new_cur_r_plan == p["trg_r"]: 
                    block_until_T_plan = (time + 1) + p["a_i"] 

                planned_actions_for_t_plus_1.append((p_idx, new_state_plan, new_cur_r_plan, new_action_finish_T_plan, aisle_to_block_plan, block_until_T_plan))
                aisle_targetted_for_t_plus_1[aisle_to_block_plan] = True
            
            else: 
                if current_r > 0: 
                    new_state_plan = "MOVING" 
                    new_cur_r_plan = current_r
                    new_action_finish_T_plan = time + 1 
                    aisle_to_block_plan = current_r
                    block_until_T_plan = time + 1
                    
                    planned_actions_for_t_plus_1.append((p_idx, new_state_plan, new_cur_r_plan, new_action_finish_T_plan, aisle_to_block_plan, block_until_T_plan))
                    aisle_targetted_for_t_plus_1[aisle_to_block_plan] = True 
        
        passengers_boarded_this_tick = 0
        for p_idx_plan, new_state_plan, new_cur_r_plan, new_action_finish_T_plan, aisle_to_block_idx_plan, block_until_T_val_plan in planned_actions_for_t_plus_1:
            p = passengers_orig[p_idx_plan]
            old_r = p["cur_r"]

            p["state"] = new_state_plan
            p["cur_r"] = new_cur_r_plan
            p["action_finish_T"] = new_action_finish_T_plan
            
            aisle_block_finish_T[aisle_to_block_idx_plan] = max(aisle_block_finish_T[aisle_to_block_idx_plan], block_until_T_val_plan)

            if old_r != new_cur_r_plan: 
                if old_r > 0 and pass_in_aisle_at_row[old_r] == p_idx_plan:
                    pass_in_aisle_at_row[old_r] = -1
                if new_cur_r_plan > 0: 
                    pass_in_aisle_at_row[new_cur_r_plan] = p_idx_plan
                
                if old_r == 0 and p["state"] != "IN_QUEUE": 
                    passengers_boarded_this_tick += 1
            else: 
                 if new_cur_r_plan > 0 and (p["state"] == "STORING_LUGGAGE" or p["state"] == "MOVING") : # If started storing or got stuck
                    pass_in_aisle_at_row[new_cur_r_plan] = p_idx_plan 
        
        boarding_q_idx += passengers_boarded_this_tick
        time += 1

    print(max_time_passenger_seated)

if __name__ == "__main__":
    main()