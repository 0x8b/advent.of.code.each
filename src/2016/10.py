import pathlib
from collections import defaultdict


data = pathlib.Path("../../data/2016/10.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


bots = defaultdict(list)

instructions = dict()

for line in lines:
    match line.strip().split(" "):
        case [
            "bot",
            bot_id,
            "gives",
            "low",
            "to",
            low_type,
            low_id,
            "and",
            "high",
            "to",
            high_type,
            high_id,
        ]:
            bot_id, low_id, high_id = int(bot_id), int(low_id), int(high_id)

            instructions[bot_id] = [(low_type, low_id), (high_type, high_id)]

        case ["value", value, "goes", "to", "bot", bot_id]:
            value, bot_id = int(value), int(bot_id)

            bots[bot_id].append(value)

        case other:
            raise ValueError(other)


outputs = defaultdict(int)


def find_ready_bots(bots):
    ready = []

    for bot_id, chips in bots.items():
        if len(chips) == 2:
            ready.append(bot_id)

    return ready


while True:
    bot_ids = find_ready_bots(bots)

    for bot_id in bot_ids:
        left_instruction, right_instruction = instructions[bot_id]

        if left_instruction[0] == "bot" and right_instruction[0] == "bot":
            if (
                len(bots[left_instruction[1]]) == 2
                or len(bots[right_instruction[1]]) == 2
            ):
                break

        bot_left_value, bot_right_value = sorted(bots[bot_id])

        if bot_left_value == 17 and bot_right_value == 61:
            part_1 = bot_id

            print("PART 1:", part_1)

        if left_instruction[0] == "bot":
            bots[left_instruction[1]].append(bot_left_value)
        else:
            outputs[left_instruction[1]] = bot_left_value

        if right_instruction[0] == "bot":
            bots[right_instruction[1]].append(bot_right_value)
        else:
            outputs[right_instruction[1]] = bot_right_value

        bots[bot_id].clear()

    if outputs[0] and outputs[1] and outputs[2]:
        part_2 = outputs[0] * outputs[1] * outputs[2]

        print("PART 2:", part_2)

        break
