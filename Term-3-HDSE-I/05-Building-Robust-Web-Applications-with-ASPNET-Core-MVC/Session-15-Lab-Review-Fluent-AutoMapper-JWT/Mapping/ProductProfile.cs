using AutoMapper;
using ShopApi.Dtos;
using ShopApi.Models;

namespace ShopApi.Mapping;

public class ProductProfile : Profile
{
    public ProductProfile()
    {
        CreateMap<Product, ProductDto>();      // CostPrice is not in the DTO, so it stays hidden
        CreateMap<SaveProductDto, Product>();
    }
}
