from setuptools import setup

setup(
    name="electrum-nmc-server",
    version="0.9",
    scripts=['run_electrum_nmc_server','electrum-nmc-server'],
    install_requires=['plyvel','jsonrpclib', 'irc'],
    package_dir={
        'electrumnmcserver':'src'
        },
    py_modules=[
        'electrumnmcserver.__init__',
        'electrumnmcserver.utils',
        'electrumnmcserver.storage',
        'electrumnmcserver.deserialize',
        'electrumnmcserver.networks',
        'electrumnmcserver.blockchain_processor',
        'electrumnmcserver.server_processor',
        'electrumnmcserver.processor',
        'electrumnmcserver.version',
        'electrumnmcserver.ircthread',
        'electrumnmcserver.stratum_tcp',
        'electrumnmcserver.stratum_http'
    ],
    description="Namecoin Electrum Server",
    author="Thomas Voegtlin",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/test123/electrum-nmc-server/",
    long_description="""Server for the Electrum Lightweight Namecoin Wallet"""
)


