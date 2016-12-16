#!/usr/bin/python

ans = []
a3 = 9
min = 1
max = 9
exclude = [a3]
for a1 in [i for i in range(min, max) if (i not in exclude)]:
    exclude.append(a1)
    for a2 in [i for i in range(min, max) if (i not in exclude)]:
        exclude.append(a2)
        for a4 in [i for i in range(min, max) if (i not in exclude)]:
            exclude.append(a4)
            for a5 in [i for i in range(min, max) if (i not in exclude)]:
                exclude.append(a5)
                for a6 in [i for i in range(min, max) if (i not in exclude)]:
                    exclude.append(a6)
                    for a7 in [i for i in range(min, max) if (i not in (exclude, 0))]:
                        exclude.append(a7)
                        for a8 in [i for i in range(min, max) if (i not in exclude)]:
                            exclude.append(a8)
                            for a9 in [i for i in range(min, max) if (i not in exclude)]:
                                if (((a1 + a2) - a3 == 4) and
                                    ((a4 - a5) * a6 == 4) and
                                    ((a7 + a8) - a9 == 4) and
                                    ((a1 + a4) / a7 == 4) and
                                    ((a2 - a5) * a8 == 4) and
                                    ((a3 - a6) - a9 == 4)
                                    ):
                                    ans.append([a1, a2, a3, a4, a5, a6, a7, a8, a9])
                            exclude.pop()
                        exclude.pop()
                    exclude.pop()
                exclude.pop()
            exclude.pop()
        exclude.pop()
    exclude.pop()

for i in range(len(ans)):
    print ans[i]