"""Tests to find stops."""
import pytest
import pyogt


stops = [
    'abisko-centrum',
    'alerydsvagen-vastra',
    'anders-ljungstedts-gymnasium',
    'anggardsskolan',
    'anggardsvagen',
    'aspeliden',
    'aspnaset-linkoping',
    'aspnasvagen',
    'barnhemsgatan',
    'berga-centrum',
    'berga-soderleden',
    'bergdalagatan-13',
    'bergdalagatan-5',
    'bergdalsgatan-linkoping',
    'bilprovningen-linkoping',
    'borggarden',
    'bostallsgatan',
    'braskens-bro',
    'bygardesgatan',
    'carl-cederstroms-gata',
    'drabantgatan',
    'drottningtorget',
    'ekdalsvagen',
    'ekhaga-linkoping',
    'ekholmens-centrum',
    'ekholmens-vardcentral',
    'ekholmsskolan',
    'ektunavagen',
    'eskadern',
    'fagelogatan',
    'fanjunkaregatan',
    'farbacksvagen',
    'farhagsvagen',
    'farsaxvagen',
    'farullsvagen',
    'flygvapenmuseum',
    'folkungavallen',
    'fonvindsvagen-ostra',
    'fonvindsvagen-vastra',
    'forskningsbyn',
    'galoppgatan',
    'gamla-linkoping',
    'gardesgatan-linkoping',
    'gullringsvagen',
    'hackefors',
    'hackefors-sodra',
    'harstenagatan',
    'hasslegatan',
    'hjulsbro-skola',
    'humlegatan',
    'isberget',
    'jakobsdal',
    'jardalavagen-50',
    'johannelunds-centrum',
    'karna-kors',
    'karna-skola',
    'karnabrunnsgatan',
    'klostergatan',
    'kristinagatan',
    'kristinebergsgatan',
    'kungsgatan-linkoping',
    'kvinnebyvagen-95',
    'landerydsvagen',
    'lansmuseet',
    'lansstyrelsen',
    'lektorshagen',
    'lillgardsgatan',
    'lindaliden',
    'linkoping-arena',
    'linkopings-resecentrum',
    'ljunghagsvagen',
    'loftgatan',
    'lotgatan',
    'lovsbergsvagen-linkoping',
    'mariebergs-vardcentral',
    'mariedalsgatan',
    'master-mattias-vag',
    'masugnen',
    'middagsgatan',
    'mjardevi-center',
    'mjardevi-linkoping',
    'morgongatan',
    'nedre-johannelund',
    'odegardsgatan-11',
    'odegardsgatan-24',
    'orkanvagen',
    'ortgatan',
    'ovre-johannelund',
    'parkgatan-linkoping',
    'pionjargatan',
    'poleraregatan',
    'raberga-bro',
    'raknestickan',
    'rattaregatan',
    'regementsgatan-linkoping',
    'risbrinksgatan',
    'rokglaset',
    'roshagsvagen',
    'rotegatan',
    'saab-civila-porten',
    'sandgardsgatan',
    'sidvindsvagen',
    'skogsfrid-linkoping',
    'slestadsskolan',
    'spangerum',
    'staby-bro',
    'stationsgatan',
    'stora-torget-linkoping',
    'stragatan',
    'strandangsvagen',
    'tallboda-centrum',
    'tallboda-skola',
    'tannefors-center',
    'tegelbruksgatan',
    'tenndosan',
    'tinnerbacksbadet',
    'tinnerbacksgrand',
    'tokarps-skola',
    'tornhagen',
    'tradgardstorget',
    'ullstamma-by',
    'universitetet-golfbanan',
    'universitetssjukhuset-norra-entren',
    'universitetssjukhuset-sodra-entren',
    'vallaplan',
    'vardsbergsvagen',
    'vetegatan-linkoping',
    'vickergatan',
    'vimarkagatan',
    'vinkannaren',
    'wernersgatan',
    'westmansgatan-66',
    'yrkesvagen',
]
stops = sorted(set(stops))


@pytest.mark.parametrize('name', stops)
def test_find_stop_by_name(name):
    """Find known stops and check that they exist."""
    stop = pyogt.find_stop(name)
    assert stop.get_name() == name
    assert stop.get_id() != -1