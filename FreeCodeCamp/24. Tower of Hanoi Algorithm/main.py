def hanoi_swaper(total_disks, source, auxiliary, destination, rods):
    steps = ''
    if(total_disks) == 1:
        destination.append(source[-1])
        source.pop()
        return (f"\n{rods[0]} {rods[1]} {rods[2]}")

    steps += hanoi_swaper(total_disks - 1, source, destination, auxiliary, rods)

    destination.append(source[-1])
    source.pop()
    steps += (f"\n{rods[0]} {rods[1]} {rods[2]}")

    steps += hanoi_swaper(total_disks - 1, auxiliary, source, destination, rods)

    return steps

def hanoi_solver(total_disks):
    steps = ''
    source = list(range(total_disks, 0, -1))
    auxiliary = []
    destination = []

    rods = [source, auxiliary, destination]

    steps += (f"{rods[0]} {rods[1]} {rods[2]}")
    steps += hanoi_swaper(total_disks, source, auxiliary, destination, rods)

    return(steps)

print(hanoi_solver(2))