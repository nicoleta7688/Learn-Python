if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    dimens = [x, y, z]
    # all_coord = []

    # for a in range(x+1):
    #     for b in range(y+1):
    #         for c in range(z+1):
    #             if(a + b + c) != n:
    #                 all_coord.append([a, b, c])
    
    all_coord = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
    
    # Construieste elementul:
    # [a, b, c]
    # pentru fiecare a
    #     pentru fiecare b
    #         pentru fiecare c
    # doar daca:
    # a + b + c != n

    print(all_coord)

"""
# List Comprehensions

Let's learn about list comprehensions!

You are given three integers `x`, `y`, and `z` representing the dimensions of a cuboid, along with an integer `n`.

Print a list of all possible coordinates given by `(i, j, k)` on a 3D grid, where:

* `0 <= i <= x`
* `0 <= j <= y`
* `0 <= k <= z`

and the sum of the coordinates is **not equal** to `n`.

Use **list comprehensions** rather than multiple loops.

## Input Format

Four integers, each on a separate line:

```
x
y
z
n
```

## Constraints

Print the list in **lexicographic increasing order**.

---

### Sample Input 0

```text
1
1
1
2
```

### Sample Output 0

```text
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

### Explanation

The possible values are:

* `i` ∈ {0, 1}
* `j` ∈ {0, 1}
* `k` ∈ {0, 1}

Generate every possible coordinate `(i, j, k)` and keep only those for which:

```text
i + j + k != n
```

---

### Sample Input 1

```text
2
2
2
2
```

### Sample Output 1

```text
[
 [0, 0, 0],
 [0, 0, 1],
 [0, 1, 0],
 [0, 1, 2],
 [0, 2, 1],
 [0, 2, 2],
 [1, 0, 0],
 [1, 0, 2],
 [1, 1, 1],
 [1, 1, 2],
 [1, 2, 0],
 [1, 2, 1],
 [1, 2, 2],
 [2, 0, 1],
 [2, 0, 2],
 [2, 1, 0],
 [2, 1, 1],
 [2, 1, 2],
 [2, 2, 0],
 [2, 2, 1]
]

"""