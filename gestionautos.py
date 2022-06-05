
test = ['azul','plateado','negro','negro','azul','plateado','negro','negro','negro']


def colors(colorsList) :
    result = []
    for color in colorsList :
        if color not in result :
            result.append(color)

    return result

print(colors(test))