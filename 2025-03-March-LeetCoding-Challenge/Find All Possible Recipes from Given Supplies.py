from collections import defaultdict, deque


class Solution:
    def findAllRecipes(
            self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        supplies = set(supplies)
        graph = defaultdict(set)  # ingredient -> recipes
        in_degree = defaultdict(int)  # recipe ->  in-degree
        queue = deque()

        for recipe, ingredient in zip(recipes, ingredients):
            not_available = 0
            for i in ingredient:
                if i not in supplies:
                    not_available += 1
                    graph[i].add(recipe)
            if not_available == 0:
                queue.append(recipe)
            else:
                in_degree[recipe] = not_available

        result = []
        while queue:
            recipe = queue.popleft()
            result.append(recipe)
            for neighbour in graph[recipe]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    queue.append(neighbour)
        return result


def main():
    recipes = ['bread']
    ingredients = [['yeast', 'flour']]
    supplies = ['yeast', 'flour', 'corn']
    assert Solution().findAllRecipes(recipes, ingredients, supplies) == ['bread']

    recipes = ['bread', 'sandwich']
    ingredients = [['yeast', 'flour'], ['bread', 'meat']]
    supplies = ['yeast', 'flour', 'meat']
    assert Solution().findAllRecipes(recipes, ingredients, supplies) == ['bread', 'sandwich']

    recipes = ['bread', 'sandwich', 'burger']
    ingredients = [['yeast', 'flour'], ['bread', 'meat'], ['sandwich', 'meat', 'bread']]
    supplies = ['yeast', 'flour', 'meat']
    assert Solution().findAllRecipes(recipes, ingredients, supplies) == ['bread', 'sandwich', 'burger']


if __name__ == '__main__':
    main()
