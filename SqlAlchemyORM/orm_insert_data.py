__author__ = 'niko'
from create_tables import Cookie,sesion

cc_cookie=Cookie(cookie_name='chocolate chip',
                cookie_recipe_url= 'http://some.aweso.me/cookie/recipe.html',
                cookie_sku='CC01',
                quantity = 12,
                unit_cost= 0.50)

sesion.add(cc_cookie)
    # Start a transaction
    # Insert the record into the database
    # The values for the insert
    # Commit the transaction

sesion.commit()


#MULTIPLE INSERT==================================================================
dcc = Cookie(cookie_name='dark chocolate chip',
             cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
             cookie_sku='CC02',
             quantity=1,
             unit_cost=0.75)

mol = Cookie(cookie_name='molasses',
             cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
             cookie_sku='MOL01',
             quantity=1,
             unit_cost=0.80)

sesion.add(dcc)
sesion.add(mol)


# A flush is like a commit;
# however, it doesnt perform a database commit and end the transaction.
#  Because of this, The dcc and mol instances are still connected to the session,
#  and can be used to perform additional database tasks without triggering additional database queries.
sesion.flush()
#==================================================================================

print(dcc.cookie_id,dcc.cookie_recipe_url)
print(mol.cookie_id,dcc.cookie_recipe_url)
