"""
Test compatibility with different SQLAlchemy versions.

This test ensures the adapter works with both SQLAlchemy 1.4.x and 2.x.
"""
import sqlalchemy
from casbin import Enforcer
from databases import Database


async def test_sqlalchemy_version_info(db: Database, enforcer: Enforcer):
    """Test that reports which SQLAlchemy version is being used."""
    print(f"\nTesting with SQLAlchemy version: {sqlalchemy.__version__}")
    
    # Verify basic enforcement works
    assert enforcer.enforce("alice", "data1", "read") == True
    assert enforcer.enforce("bob", "data2", "write") == True
    
    # This test should pass with both SQLAlchemy 1.4.x and 2.x
    major_version = int(sqlalchemy.__version__.split('.')[0])
    assert major_version in [1, 2], f"Unexpected SQLAlchemy version: {sqlalchemy.__version__}"
