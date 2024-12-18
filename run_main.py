import os

import click
import argparse

@click.command()
@click.option("--data_path", help="root path for .ply files", metavar="PATH", default="./resources/sample_scenes")
@click.option("--use2dgs", help="Use 2D Gaussian Splatting", is_flag=True, default=False)
@click.option("--mode", help="[default, decoder, attach]", default="default")
@click.option("--host", help="host address", default="127.0.0.1")
@click.option("--port", help="port", default=6009)
@click.option("--ggd_path", help="path to Gaussian GAN Decoder project", default="", type=click.Path())
def main(data_path, mode, host, port, ggd_path, use2dgs):
    if use2dgs:
        os.environ['USING_2DGS'] = 'T'
    else:
        os.environ['USING_2DGS'] = ''

    from splatviz import Splatviz
    splatviz = Splatviz(data_path=data_path, mode=mode, host=host, port=port, ggd_path=ggd_path)
    while not splatviz.should_close():
        splatviz.draw_frame()
    splatviz.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    main()
