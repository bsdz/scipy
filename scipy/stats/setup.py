from os.path import join


def configuration(parent_package='',top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('stats', parent_package, top_path)

    config.add_data_dir('tests')

    statlib_src = [join('statlib', '*.f')]
    config.add_library('statlib', sources=statlib_src)

    # add statlib module
    config.add_extension('statlib',
        sources=['statlib.pyf'],
        f2py_options=['--no-wrap-functions'],
        libraries=['statlib'],
        depends=statlib_src
    )

    # add _stats module
    config.add_extension('_stats',
        sources=['_stats.c'],
    )

    # add mvn module
    config.add_extension('mvn',
        sources=['mvn.pyf','mvndst.f'],
    )

    # add levy stable module
    config.add_library(
        'levyst',
        sources=[join('_levy_stable/c_src', 'levyst.c')],
        headers=[join('_levy_stable/c_src', 'levyst.h')]
    )
    config.add_data_files(join('_levy_stable', '*.pxd'))
    config.add_extension(
        '_levy_stable.levyst',
        libraries=['levyst'],
        sources=[join('_levy_stable', 'levyst.c')])

    return config


if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
