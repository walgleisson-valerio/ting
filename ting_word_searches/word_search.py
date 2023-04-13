def exists_word(word, instance):
    results = []
    for file in instance.data:
        result = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        for i, line in enumerate(file["linhas_do_arquivo"]):
            if word.upper() in line.upper():
                result["ocorrencias"].append({"linha": i + 1})
        if result["ocorrencias"]:
            results.append(result)
    return results

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
