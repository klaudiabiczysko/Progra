import argparse
import pickle
import yaml
from tagger import pre_process, model
import os


def run(args):
    mode = args.mode
    with open(args.config, "r") as yaml_in:
        config = yaml.load(yaml_in)

    if mode == "train":
        print(f"Training a model on {config['train_file']}.")
        X, Y = pre_process.load_dataset(config["train_file"])
        X, Y = pre_process.prepare_data_for_training(X, Y)
        tagger = model.POSTagger()
        tagger.fit_and_report(X, Y, config["crossval"], config["n_folds"])
        tagger.save_model(config["model_file"])

    elif mode == "tag":
        print(f"Tagging text using pretrained model: {config['model_file']}.")
        with open(config["model_file"], "rb") as model_in:
            tagger = pickle.load(model_in)
        # Checking if text is in os path. If so: treat as file
        if os.path.exists(args.text) and str(args.text)[-4:] == ".txt":
            outf_name = str(args.text) + '.tag'
            with open(outf_name,'w') as output_f:
                tagged_doc = tagger.tag_document(args.text)
                for sent in tagged_doc:
                    for token in sent:
                        output_f.write(f"{token[0]}\t{token[1]}".expandtabs(15))
                        output_f.write('\n')
                    output_f.write('\n')
        # If text is not a file:
        else:
            tagged_sent = tagger.tag_sentence(args.text)
            for token in tagged_sent:
                print(f"{token[0]}\t{token[1]}".expandtabs(15))

    elif mode == "eval":
        gold = args.gold
        if str(gold)[-4:] == '.tag':
            X, Y = pre_process.load_txt(gold)
        if str(gold)[-7:] == '.conllu':
            X, Y = pre_process.load_conllu(gold)
        X, Y = pre_process.prepare_data_for_training(X, Y)
        print(f"Loading model from {args.config}")
        with open(config["model_file"], "rb") as infile:
             tagger = pickle.load(infile)
        classification_rep = tagger.evaluate(X,Y)
        print (classification_rep)

    else:
        print(f"{args.mode} is an incompatible mode. Must be either 'train', 'tag' or 'eval'.")


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description="A basic SVM-based POS-tagger. \
                                     Accepts either .conllu or tab-delineated \
                                     .txt files for training.")

    PARSER.add_argument('--mode', metavar='M', type=str,
                        help="Specifies the tagger mode: {train, tag, eval}.")
    PARSER.add_argument('--text', metavar='T', type=str,
                        help="Tags a sentence string or txt file. \
                        Can only be called if '--mode tag' is specified.")
    PARSER.add_argument('--config', metavar='C', type=str,
                        help="A config .yaml file that specifies the train data, \
                        model output file, and number of folds for cross-validation.")
    PARSER.add_argument('--gold', metavar='G', type=str,
                        help="Goldstandard file. It should be a txt or conllu-file.")

    ARGS = PARSER.parse_args()

    run(ARGS)
