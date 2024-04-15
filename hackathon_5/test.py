from unstructured.partition.pdf import partition_pdf

rpe=partition_pdf(filename="Indian_Cushine-2.pdf",
                  #extract_images_in_pdf=
                  extract_images_in_pdf=True,
                  infer_table_structure=True,
                  chunking_strategy="by_title",
                  max_characters=4000,
                  new_after_n_chhars=3800,
                  combine_text_under_n_chars=2000,
                  extract_image_block_output_dir="/imgs")