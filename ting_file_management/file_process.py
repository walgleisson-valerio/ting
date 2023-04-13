from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for file in instance.data:
        if path_file == file["nome_do_arquivo"]:
            return None
    txt_imported = txt_importer(path_file)
    dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt_imported),
        "linhas_do_arquivo": txt_imported
    }
    instance.enqueue(dict)
    print(dict)


def remove(instance):
    if not instance:
        print("Não há elementos")
    else:
        file = instance.dequeue()
        print(f'Arquivo {file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
