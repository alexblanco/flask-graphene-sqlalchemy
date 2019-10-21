from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_planet
import schema_people

from database import model_planet as ModelPlanet


class Query(graphene.ObjectType):
    """Nodes which can be queried by this API."""
    node = graphene.relay.Node.Field()

    # People
    people = graphene.relay.Node.Field(schema_people.People)
    peopleList = SQLAlchemyConnectionField(schema_people.People)

    # Planet
    planet = graphene.relay.Node.Field(schema_planet.Planet)
    planetList = SQLAlchemyConnectionField(schema_planet.Planet)

    find_planet = graphene.Field(lambda: schema_planet.Planet, climate=graphene.String())

    def resolve_find_planet(self, context, climate):
        query = schema_planet.Planet.get_query(context)
        print('received param: '+climate)
        # you can also use and_ with filter() eg: filter(and_(param1, param2)).first()
        query_result = query.filter_by(climate = climate).first()
        return query_result
 
class Mutation(graphene.ObjectType):
    """Mutations which can be performed by this API."""
    # Person mutation
    createPerson = schema_people.CreatePerson.Field()
    updatePerson = schema_people.UpdatePerson.Field()

    # Planet mutations
    createPlanet = schema_planet.CreatePlanet.Field()
    updatePlanet = schema_planet.UpdatePlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
