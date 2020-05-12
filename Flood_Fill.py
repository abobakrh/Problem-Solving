class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        visited = []
        init_color = image[sr][sc]
        neighbors = self.get_neighbors(image, sr, sc, init_color)
        if neighbors == []:
            image[sr][sc] = newColor
            visited.append([sr, sc])
            return image
        for neighbor in neighbors:
            image[neighbor[0]][neighbor[1]] = newColor
            visited.append(neighbor)
            neighbors_of_old = self.get_neighbors(image, neighbor[0], neighbor[1], init_color)
            if neighbors_of_old != []:
                for n in neighbors_of_old:
                    if n not in visited:
                        neighbors.append(n)
        return image

    def get_neighbors(self, image, sr, sc, init_color):
        list_neighbors = []
        row_num, col_num = self.get_dimentions(image)
        # move up
        if sr != 0:
            list_neighbors.append([sr-1, sc])
        # move down
        if sr != row_num-1:
            list_neighbors.append([sr+1, sc])
        # move left
        if sc != 0:
            list_neighbors.append([sr, sc-1])
        # move right
        if sc != col_num-1:
            list_neighbors.append([sr, sc+1])
        return self.filter_color_neighbors(image, list_neighbors, init_color)

    def filter_color_neighbors(self, image, list_neigh, color):
        new_list = []
        for neigh in list_neigh:
            if image[neigh[0]][neigh[1]] == color:
                new_list.append(neigh)
        return new_list

    def get_dimentions(self, image):
        return len(image), len(image[0])
