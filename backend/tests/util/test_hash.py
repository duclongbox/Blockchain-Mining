from backend.utils.hash import crypto_hash


def test_crypto_hash():
    # it should return the same hash
    assert crypto_hash('one',['two',3],4) == crypto_hash('one',4,['two',3])