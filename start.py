def set_adjacent_ones(grid, i, y, rows, columns):
    if i - 1 >= 0:
        grid[i - 1][y] = 1
    if i + 1 < rows:
        grid[i + 1][y] = 1

    if y - 1 >= 0:
        grid[i][y - 1] = 1
    if y + 1 < columns:
        grid[i][y + 1] = 1

    return grid


def minimumHours(rows, columns, grid):
    minimumHoursNumber = 0
    while True:

        zero_stell = False
        for i in range(rows):
            for y in range(columns):
                print([i,y])
                if grid[i][y] == 1:
                    grid = set_adjacent_ones(grid, i, y, rows, columns)
                else:
                    zero_stell = True

        if zero_stell == False:
            break
        minimumHoursNumber += 1

    return minimumHoursNumber

grid =[
    [0,1,0],
    [0,1,0],
    [0,1,0],
    [0,1,1]
]

# print(grid[0][24] == 1)
x =minimumHours(4,3,grid)
print(x)

# def topNCompetitors(numCompetitors, topNCompetitors, competitors,
#                     numReviews, reviews):
#     competitors.sort()
#
#
#
#     competitor_occure_in_review = {}
#     for competitor in competitors:
#         competitor_occure_in_review[competitor] = 0;
#         for review in reviews:
#             if competitor in review:
#                 competitor_occure_in_review[competitor] += 1
#
#     sorted_occur = sorted(competitor_occure_in_review.items(), key=lambda kv: kv[1])
#
#     if topNCompetitors > numCompetitors:
#         return [competitor for (competitor, occur_num) in sorted_occur if occur_num > 0]
#
#     returned_competitors = [competitor for (competitor, occur_num) in sorted_occur]
#     return returned_competitors[len(returned_competitors) - topNCompetitors:]
#
#
#
#
# x = topNCompetitors(5,2,['anacell','betacellular','cetracular','deltacellular','eurocell'],3,
#                 ['Best services provided by anacell',
#                  'betacellular has great services',
#                  'anacell provides much better services than all other'])
#
# print(x)
#
#
#
#
#
# def topNCompetitors(numCompetitors, topNCompetitors, competitors,
#                     numReviews, reviews):
#     competitors.sort()
#
#
#
#     competitor_occure_in_review = {}
#     for competitor in competitors:
#         competitor_occure_in_review[competitor] = 0;
#         for review in reviews:
#             if competitor in review:
#                 competitor_occure_in_review[competitor] += 1
#
#     sorted_occur = sorted(competitor_occure_in_review.items(), key=lambda kv: kv[1], reverse=True)
#
#     if topNCompetitors > numCompetitors:
#         return [competitor for (competitor, occur_num) in sorted_occur if occur_num > 0]
#
#     returned_competitors = [competitor for (competitor, occur_num) in sorted_occur]
#     return returned_competitors[:topNCompetitors]
#
#
#
#
# y = topNCompetitors(5,2,['anacell','betacellular','cetracular','deltacellular','eurocell'],3,
#                 ['Best services provided by anacell',
#                  'betacellular has great services',
#                  'anacell provides much better services than all other'])
#
# print(y)
