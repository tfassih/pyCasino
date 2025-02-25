TODO: Clean up this absolute mess

1. ocassional edge case that results in fencepost error in pairs game, need to add error handling and fix the offending logic, but it's rare enough to be relatively unintrusive
2. need to restructure the pairs game to have proper inheritance between the pages, current solution to maintain ui context is hacky
3. need to restructure game_core for the pairs game to bind the values available to modify in the options menu
4. need to add logic to pairs game to make pairs stay visible once made and disable their respective widgets
