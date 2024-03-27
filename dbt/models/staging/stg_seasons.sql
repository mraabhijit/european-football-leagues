with 

source as (

    select * from {{ source('staging', 'seasons') }}

),

renamed as (

    select
        league_id,
        season,
        season_start_date,
        season_end_date

    from source

)

select * from renamed
