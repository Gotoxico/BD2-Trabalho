import os
import shutil

def copy_first_frames(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith("_first.jpg"):
            src = os.path.join(input_folder, filename)
            dst = os.path.join(output_folder, filename)
            shutil.copy2(src, dst)

    print("Concluído! Todos os arquivos *_first foram copiados.")

if __name__ == "__main__":
    copy_first_frames(r"C:/Users/rodri/OneDrive - Unesp/Documentos/GitHub/BD2-Trabalho/WithCLIPAndBLIP/CroppedPersons2", "OutputLowResCropsFiltered")