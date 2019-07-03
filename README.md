# Demo of Vitess with SQLAlchamy

This is a simple demo showing the basics of using Vitess with SQLALchamy.

## Instructions

1. Create the vitess cluster using cluster.yaml and the Planetscale Operator
1a. Forward the ports from the vitess cluster to your local development machine
```
kubectl port-forward service/vtctld-example-uswest 15000& kubectl port-forward service/vtctld-example-uswest 15999& kubectl port-forward service/vtgate-example-uswest 3306&
```

2. Load the lookup_vschema.json and alchemy_vschema.json files 
```
vtctlclient -server localhost:15999 ApplyVSchema -vschema "$(cat lookup_vschema.json)" lookup
vtctlclient -server localhost:15999 ApplyVSchema -vschema "$(cat alchemy_vschema.json)" lookup
```

3. Load the lookup SQL 
```
cat lookup.sql |  mysql -h 127.0.0.1 -P 3306 -u mysql_user -pmysql_password lookup
```

4. Run the sample program 
```
python schema.py
```
