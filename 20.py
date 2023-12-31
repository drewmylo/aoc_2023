from enum import Enum
from functools import partial

input = [line for line in open("input.txt", "r").read().splitlines()]
total_high = 0
total_low = 0


class Pulse(Enum):
    LOW = 1
    HIGH = 2


def add_to_pulse_count(pulse):
    global total_high
    global total_low
    if pulse == Pulse.HIGH:
        total_high += 1
    if pulse == Pulse.LOW:
        total_low += 1

modules = {}

for line in input:
    line_split = line.split('->')
    module_type = line_split[0][0]
    module_name = line_split[0][1:].strip() if line_split[0].strip() != 'broadcaster' else 'broadcaster'
    module_dests = tuple([dest.strip() for dest in line_split[1].split(',')])
    module_state = {} if module_type == '&' else Pulse.LOW if module_type == '%' else ()
    modules[module_name] = (module_name, module_type, module_dests, module_state)

#wire up conjunctions
for module in modules:
    module_name, module_type, module_dests, state = modules[module]
    for dest in module_dests:
        if dest != 'rx':
            if modules[dest][1] == '&':
                # print(modules[dest][3])
                modules[dest][3][module_name] = Pulse.LOW

for i in range(1, 999999999999999999999):
    wire = [('broadcaster', Pulse.LOW, 'button')]
    next_pulse = wire.pop(0)
    while next_pulse is not None:
        destination, pulse, source = next_pulse
        # print(source, pulse, '->', destination)
        add_to_pulse_count(pulse)
        if destination == 'rx':
            if wire:
                next_pulse = wire.pop(0)
                continue
            else:
                break
        module_name, module_type, module_dests, state = modules[destination]
        if module_name in ['kh', 'lz', 'tg', 'hn']:
            if not all(x[1] == Pulse.HIGH for x in state.items()):
                print(i, module_name, state)
        if module_type == 'b':
            for dest in module_dests:
                wire.append((dest, pulse, module_name))
        if module_type == '%':
            if pulse == Pulse.HIGH:
                pass
            else:
                if not state or pulse == Pulse.LOW:
                    state = pulse.HIGH if state == Pulse.LOW else Pulse.LOW
                for dest in module_dests:
                    wire.append((dest, state, module_name))
        if module_type == '&':
            state[source] = pulse
            if all(x[1] == Pulse.HIGH for x in state.items()):
                for dest in module_dests:
                    wire.append((dest, Pulse.LOW, module_name))
            else:
                for dest in module_dests:
                    wire.append((dest, Pulse.HIGH, module_name))
        modules[module_name] = (module_name, module_type, module_dests, state)
        if wire:
            next_pulse = wire.pop(0)
        else:
            break


# print(total_low * total_high)